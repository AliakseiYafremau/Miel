import React from "react"

export default function LoadingSVG(props) {    
    return(
        <svg width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
            <ellipse className={`fill-${props.fill}`} cx="13.2823" cy="4.37502" rx="4.12214" ry="4.37502"/>
            <ellipse className={`fill-${props.fill}`} cx="3.66412" cy="14.6875" rx="3.66412" ry="3.75002" fill="#960047"/>
            <ellipse className={`fill-${props.fill}`} cx="13.0094" cy="36.25" rx="2.9313" ry="3.12502" fill="#960047"/>
            <ellipse className={`fill-${props.fill}`} cx="4.74021" cy="27.1875" rx="3.51756" ry="3.75002" fill="#960047"/>
            <ellipse className={`fill-${props.fill}`} cx="23.8777" cy="36.875" rx="3.05344" ry="3.12502" fill="#960047"/>
            <ellipse className={`fill-${props.fill}`} cx="34.2592" cy="31.25" rx="2.44275" ry="2.50001" fill="#960047"/>
            <ellipse className={`fill-${props.fill}`} cx="37.556" cy="21.25" rx="2.44275" ry="2.50001" fill="#960047"/>
            <ellipse className={`fill-${props.fill}`} cx="35.418" cy="11.875" rx="1.83206" ry="1.87501" fill="#960047"/>
            <ellipse className={`fill-${props.fill}`} cx="31.4518" cy="6.87501" rx="1.22137" ry="1.25001" fill="#960047"/>
        </svg>
        
    )
}