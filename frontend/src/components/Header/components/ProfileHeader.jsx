import React from "react"
import { useSelector } from "react-redux"

import "./ProfileHeader.css"
import LogoutSVG from "../../SVG/Logout.jsx"


export default function ProfileHeader() {
    const manager = useSelector(state => state.Manager.manager)

    function logout() {
        localStorage.removeItem("token")
        window.location.reload()
    }
    
    return(
        <div className="header-profile">
            <div className="header-profile-data">
                <div className="photo-shadow"/>
                <div className="header-profile-photo-container">
                    <img src={`https://backend-y9b6.onrender.com/upload/photos/${manager.photo}`} alt="" className=""/>
                </div>
                <div>
                    <button onClick={logout}><LogoutSVG fill="white"/>Выход</button>
                    <div className="header-profile-infobox">
                        <div>
                            <h2><span className="bold">{manager.quotas}</span></h2><p>доступных квот</p>
                        </div>
                    </div>
                </div>
            </div>
            <div className="header-profile-info">
                <div className="header-profile-name">
                    <h4>{manager.full_name}</h4>
                </div>
                <table>
                    <thead></thead>
                    <tbody>
                        <tr><th>Офис:</th><td>{manager.office ? manager.office.name : ""}</td></tr>
                        <tr><th>Адрес:</th><td>{manager.office ? manager.office.location : ""}</td></tr>
                    </tbody>
                </table>
            </div>
        </div>
    )
}