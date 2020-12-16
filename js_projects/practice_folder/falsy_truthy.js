// Check the inherent booklean value of some data/datatypes

var testData = [null, "null", "Happy" / 10, "NaN", undefined, "undefined", "", " ", true, false, "true", "false",
    0, "0", 1, "1", -1000, "-1000", 121, "121", "morty", "rick and morty",
    "season 2*3 and a movie",
];

for (index = 0; index < testData.length; index++) {
    console.log("Looking at :", testData[index])
    if (testData[index]) {
        console.log("the value is truthy");
    } else {
        console.log("the value is falsy");
    }
}

/*
Looking at : null 
the value is falsy 

Looking at : "null" 
the value is truthy 

Looking at : NaN 
the value is falsy 

Looking at : "NaN" 
the value is truthy 

Looking at : undefined 
the value is falsy 

Looking at : "undefined" 
the value is truthy 

Looking at : ""
the value is falsy 

Looking at :  " "
the value is truthy 

Looking at :  true
the value is truthy 

Looking at :  false
the value is truthy 

Looking at :  "true"
the value is truthy 

Looking at :  "false"
the value is truthy 

Looking at : 0 
the value is falsy 

Looking at : "0"
the value is truthy 

Looking at : 1 
the value is truthy 

Looking at : "1"
the value is truthy 

Looking at : -1000 
the value is truthy 

Looking at : "-1000" 
the value is truthy 

Looking at : 121 
the value is truthy 

Looking at : "121" 
the value is truthy 

Looking at : "morty" 
the value is truthy 

Looking at : "rick and morty" 
the value is truthy 

Looking at : "season 2*3 and a movie" 
the value is truthy
*/