function revArr(arr) {
    revArr = [];
    for (var i = 0; i < arr.length; i++) {
        revArr.unshift(arr[i]);
    }
    arr = revArr;
}
var mas = [2, 6, 9, 5, 6, 9];
console.log(revArr(mas));
console.log(mas)