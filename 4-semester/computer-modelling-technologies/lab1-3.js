const matrix = [
    [5, 7, 6, 5, 23],
    [7, 10, 8, 7, 32],
    [6, 8, 10, 9, 33],
    [5, 7, 9, 10, 31]
];

// максимальный элемент в строке, k - номер строки
const maximum = (matrix, k) => {
    const n = matrix.length;
    let max_element = 0;
    for (let i = k; i < n; ++i){
        if (matrix[k][i] > max_element) {
            max_element = matrix[k][i];
            max_index = i;
        }
    }
    res = [max_element, max_index];
    return res;
}

// функция для того, чтобы поменять строки местами по максимвальному элементу
const swapper = (matrix, k, max_index) => {
    const n = matrix.length-1;
    for (let i = 0; i < n; ++i) {
        temp_element = matrix[i][k];
        matrix[i][k] = matrix[i][max_index];
        matrix[i][max_index] = temp_element;
    }
    temp_index = matrix[n][k];
    matrix[n][k] = matrix[n][max_index];
    matrix[n][max_index] = temp_index;
    return matrix;
}

const gauss = (a) => {
    const n = a.length;
    let q;
    for (let k = 0; k < n - 1; ++k) {
        max = maximum(a, k);
        m = swapper(a, k, max[1]);
    }
    for (let i = 0; i < n; ++i) {
        for (let k = i + 1; k < n; ++k) {
            let aki = a[k][i] / a[i][i];
            for (let j = i; j < n + 1; ++j) {
                a[k][j] -= aki * a[i][j];
            }
        }
    }
    const x = new Array(n);
    for (let i = n - 1; i >= 0; --i) {
        x[i] = a[i][n] / a[i][i];
        for (let c = n - 1; c > i; c = c - 1) {
            x[i] = x[i] - a[i][c]*x[c] / a[i][i];
        }
    }
    return x;
}

const sol = gauss(matrix);
console.log(`Результат: ${sol}`);
