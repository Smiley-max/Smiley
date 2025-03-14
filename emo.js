function generateSmiley() {
    const smiles = ["😊", "😄", "😁", "😃", "🙂"];
    const randomIndex = Math.floor(Math.random() * smiles.length);
    console.log(smiles[randomIndex]);
}

generateSmiley();
