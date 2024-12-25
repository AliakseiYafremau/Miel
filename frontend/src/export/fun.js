 export function declensionsQuantity(quantity, declension) {
    const remainder = quantity % 10
    if (quantity == 1 || quantity % 100 == 1) {
        return declension[0]
    }
    if ([2, 3, 4].includes(remainder) && ![12, 13, 14].includes(quantity % 100)) {
        return declension[1]
    } else {
        return declension[2]
    }
}