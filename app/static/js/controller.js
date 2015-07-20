/**
 * Created by zcfrank1st on 7/18/15.
 */
shanbay.controller('sidebarController', function ($scope, $location) {
    if ('/' === $location.path()) {
        $scope.activeA = true;
        $scope.activeB = false;
    } else if ('/learn' === $location.path()) {
        $scope.activeA = false;
        $scope.activeB = true;
    }
});

shanbay.controller('configController', function ($scope, restful, ngDialog) {
    // 暂不考虑用户登录，demo默认当前用户id为1
    restful.loadConfigs.get({userId: 1}, function(data) {
        if (data.count === "" || data.type === "") {
            $scope.type = "无";
            $scope.count = "无"
        } else {
            $scope.type = data.type;
            $scope.count = data.count;
        }
    });

    $scope.saveConfig = function () {
        // 暂不考虑用户登录，demo默认当前用户id为1
        restful.saveConfigs.save({userId: 1, type: $scope.type, count: $scope.count}, function (res) {
            if (res.info === 'yes') {
                ngDialog.open({
                    template: 'template0',
                    controller: ['$scope', function ($scope) {
                        $scope.message = "成功";
                    }]
                });
            } else {
                ngDialog.open({
                    template: 'template3',
                    controller: ['$scope', function ($scope) {
                        $scope.message = "失败";
                    }]
                });
            }
        });
    };
});


shanbay.controller('learnController', function ($scope, restful, ngDialog) {
    var total;
    var currentId;
    // 暂不考虑用户登录，demo默认当前用户id为1
    restful.loadWordsThroughConfigs.query({userId: 1}, function (data) {
        total = data;
        $scope.word = total[0].word;
        $scope.chinese = total[0].chinese;
        $scope.english = total[0].english;
        $scope.example = total[0].example;
        currentId = total[0].wordId;
    });


    $('#editor1').ace_wysiwyg({
        toolbar:
            [
                'font',
                null,
                'fontSize',
                null,
                {name:'bold', className:'btn-info'},
                {name:'italic', className:'btn-info'},
                {name:'strikethrough', className:'btn-info'},
                {name:'underline', className:'btn-info'},
                null,
                {name:'insertunorderedlist', className:'btn-success'},
                {name:'insertorderedlist', className:'btn-success'},
                {name:'outdent', className:'btn-purple'},
                {name:'indent', className:'btn-purple'},
                null,
                {name:'justifyleft', className:'btn-primary'},
                {name:'justifycenter', className:'btn-primary'},
                {name:'justifyright', className:'btn-primary'},
                {name:'justifyfull', className:'btn-inverse'},
                null,
                null,
                null,
                'foreColor',
                null,
                {name:'undo', className:'btn-grey'},
                {name:'redo', className:'btn-grey'}
            ]
    }).prev().addClass('wysiwyg-style2');

    var next = 0;
    $scope.pre = function() {
        if (next === 0) {
            ngDialog.open({ template: 'template2' });
        } else {
            next--;
            $scope.word = total[next].word;
            $scope.chinese = total[next].chinese;
            $scope.english = total[next].english;
            $scope.example = total[next].example;

            currentId = total[next].wordId;

            restful.seeSharedNotes.query({wordId: currentId}, function (data) {
                $scope.sharedComments = data;
            });
        }
    };

    $scope.next = function() {
        if (next === total.length - 1) {
            ngDialog.open({
                template: 'template1',
                controller: ['$scope','restful', function ($scope, restful) {
                    $scope.markLearnWords = function() {
                        var data = {};
                        data.userId = 1; // 默认用户id为1
                        data.wordIds = [];
                        for (var i = 0; i <= total.length -1; i++) {
                            data.wordIds.push(total[i].wordId);
                        }

                        restful.markLearnedWords.save(data, function (res) {
                            if (res.info === 'yes') {
                                $scope.closeThisDialog();
                            }
                        });
                    }
                }]
            });
        } else {
            next ++;
            $scope.word = total[next].word;
            $scope.chinese = total[next].chinese;
            $scope.english = total[next].english;
            $scope.example = total[next].example;

            currentId = total[next].wordId;

            restful.seeSharedNotes.query({wordId: currentId}, function (data) {
                $scope.sharedComments = data;
            });
        }
    };


    $scope.simpleSave = function () {
        var data = {};
        data.wordId = currentId;
        data.comments = $('#editor1').html();

        restful.saveNote.save(data, function (res) {
            if (res.info === 'yes') {
                restful.seeSharedNotes.query({wordId: currentId}, function (data) {
                    $scope.sharedComments = data;
                });
                ngDialog.open({
                    template: 'template3',
                    controller: ['$scope', function ($scope) {
                        $scope.message = "成功";
                    }]
                });
            } else {
                ngDialog.open({
                    template: 'template3',
                    controller: ['$scope', function ($scope) {
                        $scope.message = "失败";
                    }]
                });
            }
        });
    };

    $scope.saveWithShare = function () {
        var data = {};
        data.wordId = currentId;
        data.comments = $('#editor1').html();

        restful.saveAndSharedNote.save(data, function (res) {
            if (res.info === 'yes') {
                restful.seeSharedNotes.query({wordId: currentId}, function (data) {
                    $scope.sharedComments = data;
                });
                ngDialog.open({
                    template: 'template4',
                    controller: ['$scope', function ($scope) {
                        $scope.message = "成功并分享";
                    }]
                });
            } else {
                ngDialog.open({
                    template: 'template3',
                    controller: ['$scope', function ($scope) {
                        $scope.message = "失败";
                    }]
                });
            }
        });
    };

    $scope.showSharedNotes = function () {
        $scope.eye = !$scope.eye;
        if ($scope.eye === true) {
            restful.seeSharedNotes.query({wordId: currentId}, function (data) {
                $scope.sharedComments = data;
            });
        }
    };
});