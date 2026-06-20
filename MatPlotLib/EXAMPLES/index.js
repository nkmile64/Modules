// a function that reverses a string
function reverseString(str) {
    return str.split('').reverse().join('');
}

// a function that sluggifies a string
function slugify(str) {
    return str
        .toLowerCase()
        .trim()
        .replace(/[^\w\s-]/g, '')
        .replace(/\s+/g, '-')
        .replace(/-+/g, '-');
}

slugify("NIkos Mileounis&@-") // returns "nikos-mileounis"