function isLeapYear(year) {

    // Check if year is divisible by 400
    if (year % 400 === 0) {
        return "Leap Year";
    }

    // Check if year is divisible by 100
    if (year % 100 === 0) {
        return "Not a Leap Year";
    }

    // Check if year is divisible by 4
    if (year % 4 === 0) {
        return "Leap Year";
    }

    // If none of the above conditions are true
    return "Not a Leap Year";
}

// Example usage
console.log(isLeapYear(2024));
console.log(isLeapYear(1900));
console.log(isLeapYear(2000));
console.log(isLeapYear(2023));

function leap(year){
  if (year % 400 === 0 || (year % 4 === 0 && year % 100 !== 0)) {
    return "Leap Year";
  }
  return "Not a Leap Year";
}
console.log(leap(2004));
console.log(leap(2025));

