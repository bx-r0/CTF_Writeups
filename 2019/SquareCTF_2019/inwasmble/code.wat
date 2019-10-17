(module
  (type $type0 (func (result i32)))
  (memory (;0;) 1)
  (export "memory" (memory 0))
  (export "validate" (func $func0))
  (func $func0 (result i32)
    (local $var0 i32) (local $var1 i32) (local $var2 i32) (local $var3 i32)
    i32.const 0
    set_local $var0
    block $label3
      block $label0
        loop $label4
          get_local $var0
          i32.const 32
          i32.eq
          br_if $label0
          i32.const 2
          set_local $var2
          i32.const 0
          set_local $var1
          block $label1
            loop $label2
              get_local $var0
              get_local $var1
              i32.eq
              br_if $label1
              get_local $var1
              i32.const 4
              i32.mul
              i32.const 256
              i32.add
              i32.load
              get_local $var2
              i32.mul
              set_local $var2
              get_local $var1
              i32.const 1
              i32.add
              set_local $var1
              br $label2
            end $label2
          end $label1
          get_local $var0
          i32.const 4
          i32.mul
          i32.const 256
          i32.add
          get_local $var2
          i32.const 1
          i32.add
          i32.store
          get_local $var0
          i32.load8_u
          get_local $var0
          i32.const 128
          i32.add
          i32.load8_u
          i32.xor
          get_local $var0
          i32.const 4
          i32.mul
          i32.const 256
          i32.add
          i32.load8_u
          i32.ne
          br_if $label3
          get_local $var0
          i32.const 1
          i32.add
          set_local $var0
          br $label4
        end $label4
      end $label0
      i32.const 1
      return
    end $label3
    i32.const 0
  )
  (data (i32.const 128)
    "Jj[`\a0d\92}\cfB\ebF\00\17\fdP1g\1f'vwN1\94\0eg\03\da\19\bcQ"
  )
)