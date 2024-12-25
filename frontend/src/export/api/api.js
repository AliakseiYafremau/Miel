// const APIURL = "http://localhost:8000/"
const APIURL = "https://backend-y9b6.onrender.com/"

export async function post(path, body) 
{
    return await fetch(
        APIURL + path,
        {
            method: "POST",
            headers: {
                "Authorization": `${localStorage.getItem("token")}`,
            },
            body: new URLSearchParams(body)
        })
        .then(response => response.json())
        .catch(error => {return {error: error}})
}

export async function postManager(path, body) 
{
    return await fetch(
        APIURL + path,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json;charset=utf-8",
                "Authorization": `${localStorage.getItem("token")}`,
            },
            body: JSON.stringify(body)
        })
        .then(response => {
            if (response.status == 401) {
                localStorage.removeItem("token")
                location.reload()
            }
            return (response.json())
        })
        .catch(error => {return {error: error}})
}

export async function get(path) 
{    
    return await fetch(
        APIURL + path, 
        {
            method: "GET",
            headers: {
            "Authorization": `${localStorage.getItem("token")}`,
            },
        })
        .then(response => {
            if (response.status == 401) {
                localStorage.removeItem("token")
                location.reload()
            }
            return (response.json())
        })
        .catch(error => {return {error: error}})
}


// const APIURL = "https://backend-y9b6.onrender.com/"

// const token = await fetch(APIURL + "auth/login/", {
// method: "POST",  
// headers: {},
// body: new URLSearchParams({
//     email: "ermola_96@example.com",
//     password: "bO10FirD!m"
// })
// }).then((response) => response.json())

// const manager = await fetch(
// APIURL + "manager/", {
// method: "GET",
// headers: {"Authorization": `${token.access_token}`}
// }).then(response => response.json())

// const available_candidates = await fetch(
//     APIURL + "manager/get_available_candidates/", {
//     method: "GET",
//     headers: {"Authorization": `${token.access_token}`}
//     }).then(response => response.json())

// const candidates = await fetch(
// APIURL + "manager/get_candidates/", {
// method: "GET",
// headers: {"Authorization": `${token.access_token}`}
// }).then(response => response.json())

// const post = await fetch(APIURL + "invitation/invite_candidate/", {
//     method: "POST",
//     headers: {"Authorization": `${token.access_token}`},
//     body: JSON.stringify({id: 9})
//     }).then((response) => response.json())

// const post = await fetch(APIURL + "invitation/invite_candidate/", {
//     method: "POST",
//     headers: {"Authorization": `${token.access_token}`},
//     body: new URLSearchParams({id: 9}),
//     }).then((response) => response.json())