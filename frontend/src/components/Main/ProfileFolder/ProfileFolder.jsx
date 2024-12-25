import React from "react"
import { useSelector } from "react-redux"
import { useLocation } from "react-router"

import "./ProfileFolder.css"
import CandidateContainer from "../../general/CandidateContainer.jsx"


export default function ProfileFolder() {
    const candidates = useSelector(state => state.Manager.manager.candidates)

    const pathname = useLocation().pathname

    function history(candidate, id) {
        if (candidate.is_invited){
            return (<CandidateContainer candidate={candidate} key={id}/>)
        }
    }

    function favorite(candidate, id) {
        if (candidate.is_favorite){
            return (<CandidateContainer candidate={candidate} key={id}/>)
        }
    }

    React.useEffect(() => {        
    }, [])

    return(
            <div className="profile-folder">
                {pathname == "/profile/favorites" && candidates ? candidates.map((can, id) => favorite(can, id)) : ""}
                {pathname == "/profile/history" && candidates ? candidates.map((can, id) => history(can, id)) : ""}
            </div>
    )
}