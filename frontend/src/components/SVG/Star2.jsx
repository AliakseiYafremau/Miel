import React from "react"

export default function Star2SVG(props) {    
    return(
        <svg width="24" height="23" viewBox="0 0 24 23" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path className={`stroke-${props.stroke}`} d="M12.001 6.76126L12.9384 9.5421L13.3504 10.7641L14.6335 10.8932L17.6179 11.1934L15.5861 12.3637L14.1654 13.1819L14.6891 14.7356L15.5767 17.369L13.1483 15.6683L12.001 14.8648L10.8538 15.6683L8.42536 17.369L9.31303 14.7356L9.83673 13.182L8.41603 12.3637L6.38427 11.1934L9.36862 10.8932L10.6517 10.7641L11.0637 9.5421L12.001 6.76126Z" strokeWidth="4"/>
        </svg>                  
    )
}