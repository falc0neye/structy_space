const anagrams = (s1, s2) => {
    if (s1.length !== s2.length) return false;
    // s1 = s1.split('').sort().join('')
    // s2 = s2.split('').sort().join('')
    // return s1 === s2;
    const cache1 = {};
    const cache2 = {};

    for (let i = 0; i < s1.length; i++) {
        if (!cache1[s1[i]]) {
            cache1[s1[i]] = 1;
        } else {
            cache1[s1[i]]++;
        }

        if (!cache2[s2[i]]) {
            cache2[s2[i]] = 1;
        } else {
            cache2[s2[i]]++;
        }
    }
    // console.log(cache1, cache2)
    // Iterate through caches
    for (const key in cache1) {
        // console.log(key)
        // console.log(cache1[key])
        if (!cache2[key] || cache1[key] !== cache2[key]) return false;
    }
    return true;
  };

 console.log(anagrams('paper', 'reapa'));