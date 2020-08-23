import type { ToplevelViews } from "../enums/ToplevelViews";
import type { SublevelViews } from "../enums/SublevelViews";

export interface IView {
    toplevel: ToplevelViews;
    sublevel?: SublevelViews;
    data?: any;
}
