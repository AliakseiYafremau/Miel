import { createSlice } from "@reduxjs/toolkit"

const PageSlice = createSlice({
    name: "page",
    initialState: {
        page: 0,
        previousPage: 0,
        folder: 0,
        startPage: "",
        change: false
    },
    reducers: {
        setPage(state, action) {
            state.page = action.payload
        },
        setPreviousPage(state, action) {
            state.previousPage = action.payload
        },
        setFolder(state, action) {
            state.folder = action.payload
        },
        setStartPage(state, action) {
            state.startPage = action.payload
        },
        setChangePage(state, action) {
            state.change = action
        },
    }
});

export const { setPage } = PageSlice.actions
export const { setPreviousPage } = PageSlice.actions
export const { setFolder } = PageSlice.actions
export const { setStartPage } = PageSlice.actions
export const { setChangePage } = PageSlice.actions

export default PageSlice.reducer