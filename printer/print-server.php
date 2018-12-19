<?php
/**
	A Cheap-Hack Print Server
*/

header('content-type: text/plain');

//print_r($_SERVER);
//print_r($_POST);
//print_r(array_keys($_POST));
//print_r($_FILES);

$pdf_data = null;
$pdf_file = '/tmp/print.pdf';
$pdf_good = false;


// Action
switch ($_POST['a']) {
case 'print-file':

	// An Uploaded File?
	$pdf_data = file_get_contents("php://input");
	//var_dump($pdf_data);

	file_put_contents($pdf_file, $pdf_data);

	//$pdf_data = $_POST['file'];
	//move_uploaded_file($_FILES['file']['tmp_name'], $pdf_file);

	break;

case 'print-link':

	$pdf_link = $_POST['link'];
	// @todo Validate the URL against a blacklist, or known good list?
	$pdf_data = file_get_contents($pdf_link);
	file_put_contents($pdf_file, $pdf_data);
	$pdf_good = strlen($pdf_data);

	break;
}

if ($pdf_good) {

	$cmd = array('/usr/bin/lp');
	$cmd[] = '-d Star_TSP143_';
	$cmd[] = $pdf_file;
	$cmd[] = '2>&1';
	$cmd = implode(' ', $cmd);

	echo "cmd:$cmd\n";

	$buf = shell_exec($cmd);
	echo "buf:$buf\n";

	exit(0);
}
