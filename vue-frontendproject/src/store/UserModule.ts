import {User} from "@/classes/user";
import {Commit} from "vuex";

export default {
    namespaced: true,
    state: {
        user: new User()
    },
    mutations: {
        // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
        SET_USER: (state: { user: User }, user: User) => state.user = user
    },
    actions: {
        // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
        setUser: ({commit}: { commit: Commit }, user: User) => commit('SET_USER', user)
    },
}