import React from 'react';

import '../App.css';

export default function Square(props){
    return(
        <button className="square" 
        onClick = {props.onClick}>
            {props.value}
        </button>
    )
}

