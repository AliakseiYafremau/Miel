import React from "react"

export default function ArrowRightSVG(prop) {
    return(
        <svg viewBox="0 0 13 20" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path className={"fill-" + prop.fill} d="M2.025 20L0.25 18.225L8.475 10L0.25 1.775L2.025 0L12.025 10L2.025 20Z"/>
        </svg>        
    )
}