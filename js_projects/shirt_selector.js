// Lesson 3 Quiz "What do I wear?" 3-7

var testData = [
    [18, 28, 8.13, 'S'],
    [19.99, 28.99, 8.379, 'S'],
    [20, 29, 8.38, 'M'],
    [22, 30, 8.63, 'L'],
    [24, 31, 8.88, 'XL'],
    [26, 33, 9.63, '2XL'],
    [27.99, 33.99, 10.129, '2XL'],
    [28, 34, 10.13, '3XL'],
    [18, 29, 8.47, 'NA']
]

for (index = 0; index < testData.length; index++) {
    var testSet = testData[index];
    var shirtWidth = testSet[0];
    var shirtLength = testSet[1];
    var shirtSleeve = testSet[2];
    var result = "";
    // var expectedResult = testSet[3];



    if (shirtWidth >= 28 && shirtLength >= 34 && shirtSleeve >= 10.13) {
        result = "3XL";
    } else if (28 > shirtWidth && shirtWidth >= 26 && 34 > shirtLength && shirtLength >= 33 && 10.13 > shirtSleeve && shirtSleeve >= 9.63) {
        result = "2XL";
    } else if (26 > shirtWidth && shirtWidth >= 24 && 33 > shirtLength && shirtLength >= 31 && 9.63 > shirtSleeve && shirtSleeve >= 8.88) {
        result = "XL";
    } else if (24 > shirtWidth && shirtWidth >= 22 && 31 > shirtLength && shirtLength >= 30 && 8.88 > shirtSleeve && shirtSleeve >= 8.63) {
        result = "L";
    } else if (22 > shirtWidth && shirtWidth >= 20 && 30 > shirtLength && shirtLength >= 29 && 8.63 > shirtSleeve && shirtSleeve >= 8.38) {
        result = "M";
    } else if (20 > shirtWidth && shirtWidth >= 18 && 29 > shirtLength && shirtLength >= 28 && 8.38 > shirtSleeve && shirtSleeve >= 8.13) {
        result = "S";
    } else {
        result = "NA";
    }

    console.log(testSet, result);

}