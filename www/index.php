<!doctype html>
<html>
<head>
    <?php require 'head.php';?>
</head>

<body class="slide" data-type="background" data-speed="5">
    <!-- Javascript method to include navigation -->
    <nav id="nav" role="navigation"><?php include 'nav.php';?></nav>
    <!-- PHP method to include navigation -->

    <!-- Javascript method to include header -->
    <div id="header"><?php include 'header.php';?></div>
    <!-- PHP method to include header -->

<script src="/js/d3/d3.min.js"></script>
<script src="/js/d3plus/d3plus.min.js"></script>

<div class="row">
    <div class="medium-8 small-12 medium-centered columns">
        <h1>Current Games</h1>
    </div>
</div>
<div class="row">
	<ul class="medium-block-grid-2 small-block-grid-1">

<?php
    include('mysql_access.php');
    $sql = "SELECT gameId, teamOneId, teamOneScore, team1.name AS teamOneName, teamTwoId, teamTwoScore, team2.name AS teamTwoName FROM game LEFT JOIN team AS team1 ON game.teamOneId = team1.team_id LEFT JOIN team AS team2 ON game.teamTwoId = team2.team_id  WHERE active = 1;";
    $result = $db->query($sql);
    while($row = mysqli_fetch_assoc($result)) {
    	?>
    	<li>
    		<div class="small-12 columns">
    			<h4>Game <?php echo $row['gameId']; ?></h4>
    			<p><?php echo $row['teamOneName'] . ": " . $row['teamOneScore']; ?><br>
    			<?php echo $row['teamTwoName'] . ": " . $row['teamTwoScore']; ?></p>
				<?php $graphdiv = "game" . $row['gameId'];
				?>
				<div id="<?php echo $graphdiv; ?>" style="height: 500px;"></div>
				<?php
				$sql2 = "SELECT tossup, points, teamId, team.name AS teamname FROM gamedetails LEFT JOIN player ON gamedetails.playerId = player.playerId LEFT JOIN team ON player.teamId = team.team_id WHERE gameId = " . $row['gameId'] . " AND teamId = " . $row['teamOneId'] . " ORDER BY tossup ASC;";
				$result2 = $db->query($sql2);
				?>
				<script>
					var game<?php echo $row['gameId']; ?>data = [
					{'Team': '<?php echo $row['teamOneName']; ?>', 'Question Number': 0, 'Points': 0},
					{'Team': '<?php echo $row['teamTwoName']; ?>', 'Question Number': 0, 'Points': 0},
				<?php
				$round = 1;
				$points = 0;
				while ($row2 = mysqli_fetch_assoc($result2)) {
					while ($round < $row2['tossup']) {
						?>
						{'Team': '<?php echo $row2['teamname']; ?>', 'Question Number': <?php echo $round; ?>, 'Points': <?php echo $points; ?>},
						<?php
						$round += 1;
					}
					$points += $row2['points'];
					?>
					{'Team': '<?php echo $row2['teamname']; ?>', 'Question Number': <?php echo $round; ?>, 'Points': <?php echo $points; ?>},
					<?php
					$round += 1;
				}
				while ($round <= 20) {
					?>
					{'Team': '<?php echo $row['teamOneName']; ?>', 'Question Number': <?php echo $round; ?>, 'Points': <?php echo $points; ?>},
					<?php
					$round += 1;
				}
				$round = 1;
				$points = 0;
				$sql2 = "SELECT tossup, points, teamId, team.name AS teamname FROM gamedetails LEFT JOIN player ON gamedetails.playerId = player.playerId LEFT JOIN team ON player.teamId = team.team_id WHERE gameId = " . $row['gameId'] . " AND teamId = " . $row['teamTwoId'] . " ORDER BY tossup ASC;";
				$result2 = $db->query($sql2);
				while ($row2 = mysqli_fetch_assoc($result2)) {
					while ($round < $row2['tossup']) {
						?>
						{'Team': '<?php echo $row2['teamname']; ?>', 'Question Number': <?php echo $round; ?>, 'Points': <?php echo $points; ?>},
						<?php
						$round += 1;
					}
					$points += $row2['points'];
					?>
					{'Team': '<?php echo $row2['teamname']; ?>', 'Question Number': <?php echo $round; ?>, 'Points': <?php echo $points; ?>},
					<?php
					$round += 1;
				}
				while ($round <= 20) {
					?>
					{'Team': '<?php echo $row['teamTwoName']; ?>', 'Question Number': <?php echo $round; ?>, 'Points': <?php echo $points; ?>},
					<?php
					$round += 1;
				}
				?>
				]
				var game<?php echo $row['gameId']; ?>visualization = d3plus.viz()
					.container("#<?php echo $graphdiv; ?>")
					.data(game<?php echo $row['gameId']; ?>data)
					.type("line")
					.id("Team")
					.text("Team")
					.x("Question Number")
					.y("Points")
					.title("Game <?php echo $row['gameId']; ?>")
					.draw()
				</script>
			</div>
		</li>
		<?php
    }
?>

	</ul>
</div>

    <!-- Javascript method to include footer -->
    <div id="footer"><?php include 'footer.php';?></div>
    <!-- PHP method to include footer -->
</body>
</html>
