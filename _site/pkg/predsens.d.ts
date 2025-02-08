/* tslint:disable */
/* eslint-disable */
/**
 * @param {Uint8Array} _array
 * @param {number} width
 * @param {number} height
 * @param {number} sigma
 * @returns {Promise<void>}
 */
export function blur_image_and_draw_from_wasm(_array: Uint8Array, width: number, height: number, sigma: number): Promise<void>;

export type InitInput = RequestInfo | URL | Response | BufferSource | WebAssembly.Module;

export interface InitOutput {
  readonly memory: WebAssembly.Memory;
  readonly blur_image_and_draw_from_wasm: (a: number, b: number, c: number, d: number, e: number) => number;
  readonly __wbindgen_export_0: WebAssembly.Table;
  readonly __wbindgen_export_1: WebAssembly.Table;
  readonly _dyn_core__ops__function__FnMut_____Output___R_as_wasm_bindgen__closure__WasmClosure___describe__invoke__h79a9bff78e777658: (a: number, b: number) => void;
  readonly closure63_externref_shim: (a: number, b: number, c: number) => void;
  readonly __wbindgen_malloc: (a: number, b: number) => number;
  readonly __externref_table_alloc: () => number;
  readonly __wbindgen_exn_store: (a: number) => void;
  readonly closure84_externref_shim: (a: number, b: number, c: number, d: number) => void;
  readonly __wbindgen_start: () => void;
}

export type SyncInitInput = BufferSource | WebAssembly.Module;
/**
* Instantiates the given `module`, which can either be bytes or
* a precompiled `WebAssembly.Module`.
*
* @param {{ module: SyncInitInput }} module - Passing `SyncInitInput` directly is deprecated.
*
* @returns {InitOutput}
*/
export function initSync(module: { module: SyncInitInput } | SyncInitInput): InitOutput;

/**
* If `module_or_path` is {RequestInfo} or {URL}, makes a request and
* for everything else, calls `WebAssembly.instantiate` directly.
*
* @param {{ module_or_path: InitInput | Promise<InitInput> }} module_or_path - Passing `InitInput` directly is deprecated.
*
* @returns {Promise<InitOutput>}
*/
export default function __wbg_init (module_or_path?: { module_or_path: InitInput | Promise<InitInput> } | InitInput | Promise<InitInput>): Promise<InitOutput>;
