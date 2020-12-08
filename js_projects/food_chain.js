// Lesson 3 Quiz "Navigating the food chain" 3-8

var testData = [
    [true, true, "omnivore"],
    [false, true, "carnivore"],
    [true, false, "herbivore"],
    [false, false, "undefined"],
]

for (index = 0; index < testData.length; index++) {
    var testSet = testData[index];
    var eatsPlants = testSet[0];
    var eatsAnimals = testSet[1];

    /* Method #1 */
    // var category = eatsPlants && eatsAnimals ? "omnivore" : null;
    // if (category === null) {
    //     category = !eatsPlants && eatsAnimals ? "carnivore" : null;
    // }
    // if (category === null) {
    //     category = eatsPlants && !eatsAnimals ? "herbivore" : null;
    // }
    // if (category === null) {
    //     category = !eatsPlants && !eatsAnimals ? "undefined" : null;
    // }

    /* Method #2 */
    var category = eatsPlants && eatsAnimals ? "omnivore" : (!eatsPlants && eatsAnimals ? "carnivore" : (eatsPlants && !eatsAnimals ? "herbivore" : "undefined"));

    console.log(testSet[2], category);
}