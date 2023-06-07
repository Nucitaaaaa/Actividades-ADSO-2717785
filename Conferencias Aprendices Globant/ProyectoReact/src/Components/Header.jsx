
import React from 'react';
import "./Components.css"

const Header = () => {

    return (
        <>
            <header>
                <nav>
                    
                        <ul>
                            <div className='div'>
                                <li className='nav'><a href='#'>Soy</a></li>
                                <li className='nav'><a href='#'>Un</a></li>
                                <li className='nav'><a href='#'>Nav</a></li>
                            </div>
                        </ul>
                    
                </nav>
            </header>

            <h1>Actividad En <span className='span1'>React</span></h1>
        </>
    )
}

export default Header; 