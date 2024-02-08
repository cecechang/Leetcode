/**
 * @param {number} num
 * @return {number}
 */
var addDigits = function(num) {
    while(num >= 10){
        var firstDigit = Math.floor(num/10);
        var secondDigit = num - firstDigit*10;
        num = firstDigit + secondDigit;
    }
    return num;

    }
        
