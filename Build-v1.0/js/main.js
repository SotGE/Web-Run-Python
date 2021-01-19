"use strict";


/*
	Создано SotGE Ltd.
	Автор: Сорокин Максим Евгеньевич
*/


Dropzone.autoDiscover = false;


let myDropzone = new Dropzone("#upload-main__dropzone", {
	paramName: "file",
	acceptedFiles: ".jpg, .jpeg, .png",
	dictDefaultMessage: "Перетащите изображения сюда для загрузки",
	maxFiles: 10,
	maxFilesize: 5,
	addRemoveLinks: true,
	dictRemoveFile: "Удалить",
	autoProcessQueue: false,
	parallelUploads: 1
});


myDropzone.on("success", function (file) {
	console.log(file.xhr.response);
	$('#upload-main__result').empty();
	$('#upload-main__result').append(file.xhr.response);
});


myDropzone.on("complete", function (file) {
	myDropzone.removeFile(file);
});


$('#upload-main__send').click(function () {
	myDropzone.processQueue();
});
