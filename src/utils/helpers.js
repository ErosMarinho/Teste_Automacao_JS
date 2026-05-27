export const formatNumber = (num) => {
    return Number(num).toLocaleString('pt-BR', {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
    });
};

export const isEmpty = (value) => {
    return value === null || value === undefined || value.trim() === '';
};