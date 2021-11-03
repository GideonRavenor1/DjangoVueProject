import {Permissions} from "@/interfaces/permissions";

export interface Roles {
    id: number;
    permissions: Permissions[];
    name: string;
}