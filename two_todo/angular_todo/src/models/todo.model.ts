import { Guid } from "guid-typescript";

export class Todo{
    constructor(
        public id: Guid,
        public title: string,
        public desc: string,
        public isComplete: boolean,
        public showDescription: boolean
    ){ }
}