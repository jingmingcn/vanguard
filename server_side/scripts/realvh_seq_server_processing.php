<?php

/*
 * DataTables example server-side processing script.
 *
 * Please note that this script is intentionally extremely simple to show how
 * server-side processing can be implemented, and probably shouldn't be used as
 * the basis for a large complex system. It is suitable for simple use cases as
 * for learning.
 *
 * See http://datatables.net/usage/server-side for full details on the server-
 * side processing requirements of DataTables.
 *
 * @license MIT - http://datatables.net/license_mit
 */

/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
 * Easy set variables
 */

 $config = include( 'config.php' );

// DB table to use
$table = 'real_vh';

// Table's primary key
$primaryKey = 'id';

// Array of database columns which should be read and sent back to DataTables.
// The `db` parameter represents the column name in the database, while the `dt`
// parameter represents the DataTables column identifier. In this case simple
// indexes
$columns = array(
	array( 'db' => 'id', 'dt'=>0),
	array( 'db' => 'type', 'dt'=>1),
	array( 'db' => 'sequence', 'dt'=>2),
	array( 'db' => 'probability_0', 'dt'=>3),
	array( 'db' => 'probability_1', 'dt'=>4),
	array( 'db' => 'oasis_percentile_before', 'dt'=>5),
	array( 'db' => 'oasis_percentile_after', 'dt'=>6),
	array( 'db' => 'oasis_identity_before', 'dt'=>7),
	array( 'db' => 'oasis_identity_after', 'dt'=>8),
	array( 'db' => 'humanization', 'dt'=>9),
	array( 'db' => 'extinction_coefficient', 'dt'=>10),
	array( 'db' => 'hydrophobicity', 'dt'=>11),
	array( 'db' => 'molecular_weight', 'dt'=>12),
	array( 'db' => 'isoelectric_point', 'dt'=>13),
	array( 'db' => 'CDRH3', 'dt'=>14),
	array( 'db' => 'CDRH3_probability_0', 'dt'=>15),
	array( 'db' => 'CDRH3_probability_1', 'dt'=>16),
	array( 'db' => 'CDRH3_extinction_coefficient', 'dt'=>17),
	array( 'db' => 'CDRH3_hydrophobicity', 'dt'=>18),
	array( 'db' => 'CDRH3_molecular_weight', 'dt'=>19),
	array( 'db' => 'CDRH3_isoelectric_point', 'dt'=>20),
);

// SQL server connection information
$sql_details = array(
	'user' => $config->dbUser,
	'pass' => $config->dbPass,
	'db'   => $config->dbName,
	'host' => $config->dbHost
);


/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
 * If you just want to use the basic configuration for DataTables with PHP
 * server-side, there is no need to edit below this line.
 */

require( 'ssp.class.php' );

echo json_encode(
	SSP::simple( $_GET, $sql_details, $table, $primaryKey, $columns )
);


