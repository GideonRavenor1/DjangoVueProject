import {Roles} from "@/interfaces/roles";

export interface Users {
    email: string;
    first_name: string;
    id: number;
    last_name: string;
    role: Roles | any;
    username: string;
    permissions?: string[];
    fullName: any;
    canView: any
    canEdit: any


}
