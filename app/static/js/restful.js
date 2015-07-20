/**
 * Created by zcfrank1st on 7/18/15.
 */
shanbay.factory('restful', function($resource) {
    var factory = {};
    factory.saveConfigs = $resource('/app/save/configs/');
    factory.loadConfigs = $resource('/app/load/configs/:userId', {userId: '@id'});
    factory.loadWordsThroughConfigs = $resource('/app/load/words/:userId', {userId: '@id'});
    factory.saveNote = $resource('/app/save/note/');
    factory.seeSharedNotes = $resource('/app/see/notes/:wordId', {wordId: '@wordId'});
    factory.saveAndSharedNote = $resource('/app/save/and/share/');
    factory.markLearnedWords = $resource('/app/learned/words');
    return factory;
});