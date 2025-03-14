<?php
function generateSmiley() {
    $smiles = ["😊", "😄", "😁", "😃", "🙂"];
    echo $smiles[array_rand($smiles)];
}

// To generate a smiley:
generateSmiley();
?>
