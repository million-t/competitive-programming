/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    
    let memo = init
    
    const increment = () => {
        return ++init
    }
    const decrement = () => {
        return --init
    }
    const reset = () => {
        init = memo
        return init
    }
    return {
        increment: increment,
        decrement: decrement,
        reset: reset
    }
    
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */