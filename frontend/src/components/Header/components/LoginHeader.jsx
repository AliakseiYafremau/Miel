import React from "react"

import "./LoginHeader.css"
import LoginLogoSVG from "../../SVG/LoginLogo.jsx"


export default function LoginHeader() {
    
    return(
        <div className="header-login">
            <LoginLogoSVG fill="white"/>
        </div>
    )
}