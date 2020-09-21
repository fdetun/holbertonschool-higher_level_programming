#!/usr/bin/node
exports.esrever = function (list){
    let i = 0;
    let j = list.length -1;
    let arr = []

    while (i < list.length) {
        arr[i] = list[j];
        i++;
        j--;
    }
    return arr;
}
