const result1 = document.getElementById('part1');
const result2 = document.getElementById('part2');

const part1 = (input) => {
    let maxCalorie = 0;
    let current = 0;
    input.forEach((line) => {
        if (line) {
            current += parseInt(line);
        } else {
            maxCalorie = Math.max(maxCalorie, current);
            current = 0;
        }
    });
    return maxCalorie;
}

const part2 = (input) => {
    let calories = [];
    let current = 0;
    input.forEach(x => {
        if (x) {
            current += parseInt(x);
        } else {
            calories.push(current);
            current = 0;
        }
    });
    calories.sort((x, y) => y - x);
    return calories.slice(0, 3).reduce((x, y) => x + y);
}

document.getElementById("input")
  .addEventListener("change", function () {
    const fr = new FileReader();
    fr.readAsText(this.files[0]);
    fr.addEventListener('load', () => {
        const data = fr.result.split(/\r?\n/);
        result1.innerText = `part 1: ${part1(data)}`;
        result2.innerText = `part 2: ${part2(data)}`;
    })
});