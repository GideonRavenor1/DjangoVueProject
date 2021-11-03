import {Role} from "@/classes/role";
import {Entity} from "@/interfaces/entity";

export class User implements Entity {
    id: number;
    username: string;
    first_name: string;
    last_name: string;
    email: string;
    role: Role | any;
    permissions?: string[]


    constructor(id= 0, username = '', first_name = '',
                last_name = '', email = '', role = new Role(), permissions: string[] = []) {
        this.id = id;
        this.username = username;
        this.first_name = first_name;
        this.last_name = last_name;
        this.email = email;
        this.role = role
        this.permissions = permissions

    }
    get fullName(): string {
        return this.first_name + ' ' + this.username + ' ' + this.last_name
    }
    // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
    canView(page: string) {
        if(this.permissions){
            return this.permissions.some(p => p === `view_${page}`);
        }

    }
    // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
    canEdit(page: string) {
        if(this.permissions){
            return this.permissions.some(p => p === `edit_${page}`);
        }

    }

}