// Get the display element
const display = document.getElementById('display');

// Append user input to the display
function appendToDisplay(input) {
    display.value += input;
    // console.log(display.value);
}

// Calculate the result using `eval` (with error handling)
function calculate() {
    try {
        display.value = eval(display.value) || '';
    } catch (error) {
        display.value = 'ERROR';
    }
}

// Clear the display
function clearDisplay() {
    display.value = '';
}
