// Keyboard Matrix

// rows are inputs
byte rows[] = {2,3,4,5,6,7,8,9};
const int rowCount = sizeof(rows)/sizeof(rows[0]);

//columns are outputs.  
byte cols[] = {22,24,26,28,30,32,34,36};
const int colCount = sizeof(cols)/sizeof(cols[0]);
 
byte keys[colCount][rowCount];
byte lastKeys[colCount][rowCount];

void setup() {
    Serial.begin(9600);
    Serial.println("Initialized");

    for (int colIndex=0; colIndex < colCount; colIndex++) { //fills with unpressed as inital state
      for (int rowIndex=0; rowIndex < rowCount; rowIndex++) {
        lastKeys[colIndex][rowIndex] = 1;
    }
  }
}
 
void readMatrix() {
    // iterate the columns
    for (int colIndex=0; colIndex < colCount; colIndex++) {
        // col: set to output to low
        byte curCol = cols[colIndex];
        pinMode(curCol, OUTPUT);
        digitalWrite(curCol, LOW);
 
        // row: interate through the rows
        for (int rowIndex=0; rowIndex < rowCount; rowIndex++) {
            byte rowCol = rows[rowIndex];
            pinMode(rowCol, INPUT_PULLUP);
            delay(1);
            keys[colIndex][rowIndex] = digitalRead(rowCol);
            pinMode(rowCol, INPUT);
        }
        // disable the column
        pinMode(curCol, INPUT);
    }
} 

void storeLastMatrix() {
  for (int colIndex=0; colIndex < colCount; colIndex++) {
    for (int rowIndex=0; rowIndex < rowCount; rowIndex++) {
      lastKeys[colIndex][rowIndex] = keys[colIndex][rowIndex];
    }
  }
}
 
void printMatrix() {
    for (int rowIndex=0; rowIndex < rowCount; rowIndex++) { //samples all rows
        for (int colIndex=0; colIndex < colCount; colIndex++) {  //samples all columns
            if (keys[colIndex][rowIndex] == 0 && lastKeys[colIndex][rowIndex] == 1) {
              String StrVal = "P" + String(colIndex) + "," + String(rowIndex); //concatonate coordinate of button press
              Serial.println(StrVal); //adds new line so if multiple buttons are pressed, it still works.
            }
            else if (keys[colIndex][rowIndex] == 0 && lastKeys[colIndex][rowIndex] == 0) {
              
            }
            else if (keys[colIndex][rowIndex] == 1 && lastKeys[colIndex][rowIndex] == 1) {
              
            }
            else if (keys[colIndex][rowIndex] == 1 && lastKeys[colIndex][rowIndex] == 0) {
              String StrVal = "R" + String(colIndex) + "," + String(rowIndex); //concatonate coordinate of button press
              Serial.println(StrVal); //adds new line so if multiple buttons are pressed, it still works.
            }   
        }   
    }
    storeLastMatrix(); //stores before read for state machine
}
 
void loop() {
    readMatrix();
    printMatrix();
    delay(50); //not too quickly; can be changed
}
