<?php
$pdo = new PDO ( 'mysql:host=localhost;dbname=meichu;charset=utf8', 'meichu', 'meichu13579meichu' );
$sql = $pdo->prepare ( 'insert into messages(user, msg, timestamp) values (?, ?, ?)' );
$sql->execute([urldecode($_GET['user']), urldecode($_GET['msg']), time()]);
?>
