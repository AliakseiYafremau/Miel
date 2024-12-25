import React from "react"

export default function StickyNoteSVG(props) {    
    return(
        <svg viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path className={`fill-${props.fill}`} d="M13 18H2C1.45 18 0.979167 17.8042 0.5875 17.4125C0.195833 17.0208 0 16.55 0 16V2C0 1.45 0.195833 0.979167 0.5875 0.5875C0.979167 0.195833 1.45 0 2 0H16C16.55 0 17.0208 0.195833 17.4125 0.5875C17.8042 0.979167 18 1.45 18 2V13L13 18ZM12 16V14C12 13.45 12.1958 12.9792 12.5875 12.5875C12.9792 12.1958 13.45 12 14 12H16V2H2V16H12ZM8 13H10V7H13V5H5V7H8V13Z"/>
        </svg>        
    )
}