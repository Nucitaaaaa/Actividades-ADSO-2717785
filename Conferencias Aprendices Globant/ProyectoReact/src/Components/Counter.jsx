
import React, { useState } from 'react';
import "./Components.css"

const Counter = () => {
    const [count, setCount] = useState(0);

    const handleIncrement = () => {
        setCount(count + 1)
    };

    const handleDecrement = () => {
        setCount(count - 1)
    }

    return (
        <>
            <h2>Contador</h2>
            <p className='pCounter'>El valor actual es <span className='span2'>{count}</span></p>
            <div className='divButton1'>
                <button className='Button1' onClick={handleDecrement}>Decrementar</button>
                <button className='Button2' onClick={handleIncrement}>Incrementar</button>
            </div>
        </>
    )
}

export default Counter;







