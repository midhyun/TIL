const foo = 'bar'

function add(a: number, b: number): number {
    return a + b
}

type A = {
    type: 'a',
    content: string,
}

type B = {
    type: 'b',
    content: number,
}

interface C {
    type: 'a',
    content: string,
}

type D = string | number

function detect(obj: A | B | C ) {
    if (obj.type === 'a') {
        console.log(obj.content)
    } else {
        console.log(obj.content)
    }
}