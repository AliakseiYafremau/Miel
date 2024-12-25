import React from "react"
import { Route, Routes } from "react-router-dom"

import "./Header.css"
import LoginHeader from "./components/LoginHeader.jsx"
import ProfileHeader from "./components/ProfileHeader.jsx"
import DashBoardHeader from "./components/DashBoardHeader.jsx"
import CandidateHeader from "./components/CandidateHeader.jsx"
import ProfileFolderHeader from "./components/ProfileFolderHeader.jsx"


export default function Header() {
    
    return(
        <header>
            <div className="header-container">
            <Routes>
                <Route path="login" element={<LoginHeader/>} />
                <Route path="home" element={<DashBoardHeader/>} />
                <Route path="profile" element={<ProfileHeader/>} />
                <Route path="profile/*" element={<ProfileFolderHeader/>} />
                <Route path="candidate" element={<CandidateHeader/>} />
            </Routes>
            </div>
        </header>
    )
}