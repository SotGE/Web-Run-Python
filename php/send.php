<?php
	/*
		Создано SotGE Ltd.
		Автор: Сорокин Максим Евгеньевич
	*/


	$directory = "../upload/";


	if (!is_dir($directory)) {
		mkdir($directory, 0777, true);
	}


	$temp = $_FILES['file']['tmp_name'];
	$name = basename($_FILES["file"]["name"]);
	$file = $directory.$name;
	move_uploaded_file($temp, $file);


	$command = escapeshellcmd("C:\Users\sotge\Downloads\WPy64-3910\python-3.9.1.amd64\python.exe ../python/update.py $name");
	$output = shell_exec($command);


	if ($output) {
		echo "<img class='upload-main__img' src='/upload/$output' alt='$output' srcset='/upload/$output'>";
	}
?>
