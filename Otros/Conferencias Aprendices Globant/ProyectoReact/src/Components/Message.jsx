
import React, { useState } from 'react';

const Message = ({text}) => {
    const [showMessage, setShowMessage] = useState(false);

    const handleClick = () => {
        setShowMessage(!showMessage);
    };

    return (
        <>
            <div className='divButton3'>
                <button className='button4' onClick = {handleClick}>Mostrar/Ocultar</button>
                {showMessage && <p>{text}</p>}
            </div>
        </>
    );
}

export default Message
