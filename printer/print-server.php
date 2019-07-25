<?php
/**
 * A Cheap-Hack Print Server
 */

$printer_name = 'Zebra_Technologies_ZTC_LP_2824_Plus';


header('content-type: text/plain');
header('x-openthc: print-server');

switch ($_SERVER['REQUEST_METHOD']) {
case 'GET':

	$printer_info = shell_exec('/usr/bin/lpstat -s');

	$printer_list = array();

	if (preg_match_all('/^device for (\w+): (.+)$/m', $printer_info, $m)) {
		// print_r($m);
		foreach ($m[1] as $p) {
			$printer_list[] = $p;
		}
	}

	// Show the Known Printers?
	echo "POST a FILE or LINK to print\n";
	echo "\n";
	echo "Default Printer: $printer_base\n";
	echo "Other Printers:\n  ";
	echo implode("\n  ", $printer_list);
	echo "\n";
	// var_dump($printer_list);


	break;
case 'POST':
	// OK
	break;
default:
	header('HTTP/1.1 405 Not Allowed', true, 405);
	echo "Not Allowed\n";
	exit(0);
}

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
	$cmd[] = sprintf('-d %s', escapeshellarg($printer_name)); // '-d Star_TSP143_';
	$cmd[] = escapeshellarg($pdf_file);
	$cmd[] = '2>&1';
	$cmd = implode(' ', $cmd);

	echo "cmd:$cmd\n";

	$buf = shell_exec($cmd);
	echo "buf:$buf\n";

	exit(0);
}
