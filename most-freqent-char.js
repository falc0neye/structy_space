const mostFrequentChar = (s) => {
    let maxFreq = 0;
    let maxFreqChar = '';
    let maxFreqMinIndex = Infinity;
    let cache = {
    };
    
    for (let i = 0; i < s.length; i++) {
        // If same char, increment and continue
        console.log(s[i])
        console.log(maxFreq)
        console.log(maxFreqChar)
        if (!cache[s[i]]) {
            console.log(s[i])
            cache[s[i]] = {
                count: 1,
                minIndex: i
            }
        } else {
            console.log(s[i])
            cache[s[i]].count++
            if (cache[s[i]].count >= maxFreq && cache[s[i]].minIndex < cache[maxFreqChar].minIndex) {
                console.log(s[i])
                maxFreq = cache[s[i]].count;
                maxFreqChar = s[i];
            }
        }
        if (cache[s[i]].count > maxFreq) {
            console.log(s[i])
            maxFreq = cache[s[i]].count;
            maxFreqChar = s[i];
        }

    }
    console.log({maxFreqChar, maxFreq})
    console.log(cache)
    return maxFreqChar;
  };

//   console.log(mostFrequentChar('bookeeper')); // -> 'e'
  console.log(mostFrequentChar('mississippi')); // -> 'd'