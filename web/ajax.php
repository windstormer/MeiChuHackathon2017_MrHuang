<?php
$pdo = new PDO ( 'mysql:host=localhost;dbname=meichu;charset=utf8', 'meichu', 'meichu13579meichu' );
$sql = $pdo->prepare ( 'insert into users(id, ip, mac, timestamp) values (?, ?, ?, ?)' );
$sql->execute([$_POST['id'], $_POST['ip'], $_POST['mac'], time()]);
?>