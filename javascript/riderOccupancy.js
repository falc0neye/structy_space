const myStr = 'abbcac';

function maxOccupancy(str, target) {
    const rider = {
        id: target,
        count: 0,
        firstIndex: Infinity,
    }
    const cache = {};
    let maxOccupancy = 1;
    let slate = [];

    for (let i = 0; i < str.length; i++) {
        // Conditionals for current rider
        if (str[i] === rider.id) {
            if (rider.count === 0) {
                rider.count++;
                rider.firstIndex = i;
                slate.push(maxOccupancy)
                continue
            }
            if (rider.count === 1) {
                rider.count++
                console.log('here')
                console.log(slate)
                return slate
            }
        }
        // Conditionals for non-riders
        if (!cache[str[i]] && str[i] !== rider.id) {
            console.log('here', str[i])
            cache[str[i]] = {
                id: str[i],
                count: 1,
                firstIndex: i,
            };
            maxOccupancy++
            if (cache[str[i]].firstIndex > rider.firstIndex) {
                slate.push(maxOccupancy)
            }
            continue
        } else {
            cache[str[i]].count++
            maxOccupancy--
            continue
        } 
    }
}

console.log(maxOccupancy(myStr, 'b'))