import { createSlice } from "@reduxjs/toolkit"


const HeaderToggleSlice = createSlice({
    name: "header_toggle",
    initialState: {
        header_toggle: true,
    },
    reducers: {
        setHeaderToggle(state, action) {
            state.header_toggle = action.payload
        }
    }
});

export const { setHeaderToggle } = HeaderToggleSlice.actions;

export default HeaderToggleSlice.reducer;